from __future__ import annotations

from typing import Callable, Dict, List


class Cell:
    '''
    Contain a value accessed by other listening cells.

    Attributes:
        value: value contained by cell
        _listeners: cells which are recomputed if value is changed
    '''

    def __init__(self, initial_value: int):
        '''
        Set initial value of self and allow for listeners to be added.

        Parameters:
            initial_value: value used to first define self
        '''
        self._value = initial_value
        self._listeners = set()

    def add_listener(self, cell: Cell) -> None:
        '''Add a cell to listeners of self.'''
        self._listeners.add(cell)

    def update_listeners(self, old_values: Dict[Cell, int]):
        '''Recompute values of listeners according to values in changed.'''
        for listener in self._listeners:
            listener.recompute(old_values)

    @property
    def value(self) -> int:
        '''Value contained by Cell object.'''
        return self._value


class InputCell(Cell):
    '''
    A cell with a value that is independent of other cells, and which influences
    the values of listening ComputeCells.

    Attributes:
        value, _listeners: (see Cell())
    '''
    @Cell.value.setter
    def value(self, new_value):
        '''Updates values of listening cells and calls callbacks.'''
        if new_value != self.value:
            self._value = new_value
            old_values = {}
            self.update_listeners(old_values)
            for cell, old_value in old_values.items():
                if cell.value != old_value:
                    cell.call_callbacks()


class ComputeCell(Cell):
    '''
    A cell with a value equal to output of compute_function(inputs). 
    Value automatically changes when cells in inputs change.

    Attributes:
        value, _listeners: (see Cell())
        _inputs, _compute_function: see self.__init__()
        _callbacks: functions to be called when value is changed
    '''

    def __init__(self,
                 inputs: List[InputCell],
                 compute_function: Callable[[List[int]], int]):
        '''
        Adds self as listener to InputCells in inputs and computes value to be
        contained.

        Parameters:
            inputs: InputCells used to calculate value of self
            compute_function: outputs value of self given _inputs
        '''
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = set()
        for cell in inputs:
            cell.add_listener(self)
        super().__init__(self.compute())

    def add_callback(self, callback: Callable) -> None:
        '''Add callback function to list of callbacks.'''
        self._callbacks.add(callback)

    def remove_callback(self, callback):
        '''Remove callback function from list of callbacks.'''
        self._callbacks.discard(callback)

    def compute(self) -> List[int]:
        '''Return value contained by self.'''
        return self._compute_function([cell.value for cell in self._inputs])

    def recompute(self, old_values: Dict[Cell, int]) -> None:
        '''Check if value needs to be updated and updates listeners.'''
        if (new_value := self.compute()) != self.value:
            old_values.setdefault(self, self.value)
            self._value = new_value
            self.update_listeners(old_values)

    def call_callbacks(self):
        '''Run all callback functions with value of self as input.'''
        for callback in self._callbacks:
            callback(self.value)
