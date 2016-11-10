import sys
import traceback
from os.path import basename

import colorama
from colorama import Fore, Style


# TODO: Allow to enable backtrace by setting an environment variable.


def _flush_message(message):
    """Flush the message to stdout.
    """
    sys.stderr.write(message + '\n')
    sys.stderr.flush()


def _name_module(module):
    """Replace `<module>` at the beginning of the trace with the
    name of the calling file.
    """
    # return module if module != "<module>" else __file__
    return module


def _build_flow(entries):
    flow = []
    for entry in entries:
        flow.append('{0}{1}{2}{3} ({4})\n'.format(
            Fore.GREEN,
            _name_module(entry[2]),
            Fore.WHITE,
            Style.DIM,
            entry[3]))
    directed_flow = ' {0} --> '.format(Fore.YELLOW).join(flow)
    _flush_message(directed_flow)


class Hook(object):
    def __init__(self,
                 entries,
                 align=False,
                 flow_only=False,
                 strip_path=False):
        self.entries = entries
        self._align = align
        self._strip = strip_path

    def reverse(self):
        self.entries = self.entries[::-1]

    def generate_backtrace(self):
        file_format = Style.DIM
        line_format = Fore.RED + Style.BRIGHT
        context_format = Fore.GREEN
        call_format = Fore.YELLOW + ' --> '

        rebuilt_traceback = []
        for entry in self.entries:
            rebuilt_traceback.append((
                file_format + basename(entry[0]) if self._strip else entry[0],
                line_format + str(entry[1]),
                context_format + _name_module(entry[2]),
                call_format + entry[3]))

        lengths = self._set_alignment(rebuilt_traceback) if \
            self._align else [1, 1, 1, 1]

        backtrace_entries = []

        for entry in rebuilt_traceback:
            backtrace_entries.append(
                '{0:{1}} {2:{3}} {4:{5}} {6:{7}}'.format(
                    entry[0], lengths[0],
                    entry[1], lengths[1],
                    entry[2], lengths[2],
                    entry[3], lengths[3]))
        return backtrace_entries

    def _set_alignment(self, entries):
        lengths = [0, 0, 0, 0]

        for entry in entries:
            for index, field in enumerate(entry):
                lengths[index] = max(lengths[index], len(str(entry[index])))
        return lengths


def rehook(reverse=False,
           flow_only=False,
           align=False,
           strip_path=False):

    colorama.init(autoreset=True)

    def new_excepthook(tpe, value, tb):
        traceback_entries = traceback.extract_tb(tb)
        hook = Hook(traceback_entries, align=align, strip_path=strip_path)

        _flush_message(Fore.YELLOW + 'Traceback: ({0})'.format(
            'Most recent call first' if reverse
            else 'Most recent call last'))
        main_message = '{0}{1}{2}: {3}'.format(
            Fore.RED,
            Style.BRIGHT,
            tpe.__name__,
            str(value))

        if reverse:
            hook.reverse()
        backtrace = hook.generate_backtrace()
        backtrace.insert(0 if reverse else len(backtrace), main_message)
        for entry in backtrace:
            _flush_message(entry)

    sys.excepthook = new_excepthook
