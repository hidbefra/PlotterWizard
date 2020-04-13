import model_Offset
import model_Schnittparameter
import model_Prozess


class Arbeitsschritt:

    anzahl = 0

    def __init__(self, name=None, enabled=None, offset=None, schnittparameter=None):
        Arbeitsschritt.anzahl += 1

        if name is None:
            self.name = "Arbeitsschritt" + Arbeitsschritt.anzahl.__str__()
        else:
            self.name = name

        if enabled is None:
            self.enabled = 2
        else:
            self.enabled = enabled

        self.offset = model_Offset.Offset()
        if isinstance(offset, dict):
            self.offset.__init__(**offset)
        elif isinstance(offset, model_Offset.Offset) and offset is not None:
            self.offset = offset

        self.schnittparameter = model_Schnittparameter.Schnittparameter()
        if isinstance(schnittparameter, dict):
            self.schnittparameter.__init__(**schnittparameter)
        elif isinstance(schnittparameter, model_Schnittparameter.Schnittparameter) and schnittparameter is not None:
            self.schnittparameter = schnittparameter






