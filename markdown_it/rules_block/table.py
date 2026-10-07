from __future__ import annotations
import re
from ..common.utils import charStrAt, isStrSpace, mdTrim
from .state_block import StateBlock
headerLineRe = re.compile('^:?-+:?$')
enclosingPipesRe = re.compile('^\\||\\|$')
MAX_AUTOCOMPLETED_CELLS = 65536

def getLine(state: StateBlock, line: int) -> str:
    """本函数体在基线里被有意移除，请按题面要求重新实现。"""
    raise NotImplementedError()

def escapedSplit(string: str) -> list[str]:
    """本函数体在基线里被有意移除，请按题面要求重新实现。"""
    raise NotImplementedError()

def table(state: StateBlock, startLine: int, endLine: int, silent: bool) -> bool:
    """本函数体在基线里被有意移除，请按题面要求重新实现。"""
    raise NotImplementedError()
