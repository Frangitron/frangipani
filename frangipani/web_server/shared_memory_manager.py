import struct

from multiprocessing.shared_memory import SharedMemory

from frangipani_web_server.control import Group
from frangipani_web_server.control.base.base_input import BaseInputControl
from frangipani_web_server.control.base.base import BaseControl


class SharedMemoryManager:

    def __init__(self, root_control_definition: BaseControl):
        self._root_control_definition = root_control_definition
        self._memory: SharedMemory | None = None
        self._control_map: dict[str, tuple[int, str]] = {}
        self._buffer_size = 0
        self._build_map()

    def _build_map(self):
        self._control_map = {}
        self._buffer_size = 0

        def traverse(control: BaseControl):
            if isinstance(control, BaseInputControl):
                fmt = ""
                # bool is a subclass of int, so check bool first
                if isinstance(control.value, bool):
                    fmt = "?"
                elif isinstance(control.value, (int, float)):
                    fmt = "d"

                if fmt:
                    self._control_map[control.address] = (self._buffer_size, fmt)  # TODO make this a dataclass
                    self._buffer_size += struct.calcsize(fmt)

            elif isinstance(control, Group):
                for child in control.controls:
                    traverse(child)

        traverse(self._root_control_definition)

    @property
    def control_map(self) -> dict[str, tuple[int, str]]:
        return self._control_map

    def create_from_controls(self) -> str:
        """
        Creates a SharedMemory object from control definitions

        :return: the SharedMemory name
        """
        self._assert_not_created()
        size = max(1, self._buffer_size)
        self._memory = SharedMemory(create=True, size=size)
        self._write_initial_values()
        return self._memory.name

    def _write_initial_values(self):
        def traverse(control: BaseControl):
            if isinstance(control, BaseInputControl) and control.address in self._control_map:
                offset, fmt = self._control_map[control.address]
                val = control.value
                struct.pack_into(fmt, self._memory.buf, offset, val)

            if isinstance(control, Group):
                for child in control.controls:
                    traverse(child)

        traverse(self._root_control_definition)

    def create_from_name(self, name: str) -> None:
        """
        Creates a SharedMemory object from an existing name

        :param name: Name of the shared memory
        :return: None
        """
        self._assert_not_created()
        self._memory = SharedMemory(name=name)

    def get_value(self, control_address: str) -> float | bool:
        if control_address not in self._control_map:
            raise KeyError(f"Control {control_address} not found in shared memory map")

        offset, fmt = self._control_map[control_address]
        return struct.unpack_from(fmt, self._memory.buf, offset)[0]

    def get_all_values(self) -> dict[str, float | bool]:
        result = {}
        for control_id, (offset, fmt) in self._control_map.items():
            val = struct.unpack_from(fmt, self._memory.buf, offset)[0]
            result[control_id] = val
        return result

    def cleanup(self):
        if self._memory is not None:
            self._memory.close()
            self._memory.unlink()
            self._memory = None

    def _assert_not_created(self):
        if self._memory is not None:
            raise RuntimeError(f"Shared memory already created ({self._memory.name})")
