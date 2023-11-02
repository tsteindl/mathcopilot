# mathcopilot
Python project that detects handwritten equations and mathematical statements in a program like Xournal++/OneNote, calls Mathematica or any other mathematical software and displays the calculated result.

## Dependencies
- Uses mathpix to parse handwritten equation to latex
- Uses wolframclient (""[]) to evaluate expressions

https://github.com/xournalpp/xournalpp/issues/2747

```
npm install -g @mathpix/mpx-cli
mpx login
```
## TODO
### Python
- configurable API to wolfram alpha
- text detection to latex expression
- parser from latex expression to mathematica expression (mathematica supports this)
### C++
- get xournalpp fork running
- xournalpp text detection
- UI
  - On/Off switch
  - Configuration button (path to wolfram,...)
  - Popup that shows detected latex expression and enables copying
  - Popup that shows calculated expression
  - option to open mathematica in current context
### Javascript/?
- onenote plugin
