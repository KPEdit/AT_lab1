# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : laba1.sm

from . import statemap


class LabaState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def asg(self, fsm):
        self.Default(fsm)

    def end(self, fsm):
        self.Default(fsm)

    def name(self, fsm, nm):
        self.Default(fsm)

    def num(self, fsm, nm):
        self.Default(fsm)

    def type(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class LabaMap_Default(LabaState):

    def name(self, fsm, nm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Error)
        fsm.getState().Entry(fsm)


    def num(self, fsm, nm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Error)
        fsm.getState().Entry(fsm)


    def end(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Error)
        fsm.getState().Entry(fsm)


    def type(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Error)
        fsm.getState().Entry(fsm)


    def asg(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Error)
        fsm.getState().Entry(fsm)


class LabaMap_Start(LabaMap_Default):

    def num(self, fsm, nm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.setLine(nm)
        finally:
            fsm.setState(LabaMap.Line)
            fsm.getState().Entry(fsm)


class LabaMap_Line(LabaMap_Default):

    def name(self, fsm, nm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.setName(nm)
        finally:
            fsm.setState(LabaMap.VarName)
            fsm.getState().Entry(fsm)


    def type(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.VarType)
        fsm.getState().Entry(fsm)


class LabaMap_VarName(LabaMap_Default):

    def asg(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.Assign)
        fsm.getState().Entry(fsm)


    def end(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.OK)
        fsm.getState().Entry(fsm)


class LabaMap_VarType(LabaMap_Default):

    def name(self, fsm, nm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.setName(nm)
        finally:
            fsm.setState(LabaMap.VarName)
            fsm.getState().Entry(fsm)


class LabaMap_Assign(LabaMap_Default):

    def name(self, fsm, nm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.NameValue)
        fsm.getState().Entry(fsm)


    def num(self, fsm, nm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.NumValue)
        fsm.getState().Entry(fsm)


class LabaMap_NumValue(LabaMap_Default):

    def end(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.OK)
        fsm.getState().Entry(fsm)


class LabaMap_NameValue(LabaMap_Default):

    def end(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(LabaMap.OK)
        fsm.getState().Entry(fsm)


class LabaMap_OK(LabaMap_Default):
    pass

class LabaMap_Error(LabaMap_Default):
    pass

class LabaMap(object):

    Start = LabaMap_Start('LabaMap.Start', 0)
    Line = LabaMap_Line('LabaMap.Line', 1)
    VarName = LabaMap_VarName('LabaMap.VarName', 2)
    VarType = LabaMap_VarType('LabaMap.VarType', 3)
    Assign = LabaMap_Assign('LabaMap.Assign', 4)
    NumValue = LabaMap_NumValue('LabaMap.NumValue', 5)
    NameValue = LabaMap_NameValue('LabaMap.NameValue', 6)
    OK = LabaMap_OK('LabaMap.OK', 7)
    Error = LabaMap_Error('LabaMap.Error', 8)
    Default = LabaMap_Default('LabaMap.Default', -1)

class Laba_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, LabaMap.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
