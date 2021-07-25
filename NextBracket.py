import sublime;
import sublime_plugin;


class NextBracketCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward):
        newPoint = None;

        if forward:
            newPoint = self.__findNextBracket();
        else:
            newPoint = self.__findPreviousBracket();
        
        if newPoint:
            self.view.sel().clear();
            self.view.sel().add(sublime.Region(newPoint.end()));
            self.view.show(newPoint);
        
    def __findNextBracket(self):
        allBracketPoints = self.view.find_all(self.__getRegex());
        result = None;

        for potentialPoint in allBracketPoints:
            if self.view.rowcol(potentialPoint.begin())[0] > self.__getCaretLine():
                if result == None or self.view.rowcol(potentialPoint.begin())[0] == self.view.rowcol(result.begin())[0]:
                    result = potentialPoint;
                else:
                    break;

        return result;

    def __findPreviousBracket(self):
        allBracketPoints = self.view.find_all(self.__getRegex());
        result = None;

        for potentialPoint in reversed(allBracketPoints):
            if self.view.rowcol(potentialPoint.begin())[0] < self.__getCaretLine():
                result = potentialPoint;

                break;

        return result;

    def __getCaretLine(self):
        return self.view.rowcol(self.view.sel()[0].begin())[0];

    def __getRegex(self):
        settings = sublime.load_settings("NextBracket.sublime-settings");
        regex = "[";
        
        if settings.get('include_square_brackets'):
            regex = regex + "\\[\\]"
        
        if settings.get('include_round_brackets'):
            regex = regex + "{}"
        
        if settings.get('include_curly_brackets'):
            regex = regex + "()"

        if settings.get('include_angle_brackets'):
            regex = regex + "<>"

        return regex + "]"
