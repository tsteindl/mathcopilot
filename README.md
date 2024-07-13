# mathcopilot
Python project that detects handwritten equations and mathematical statements in a program like Xournal++/OneNote, calls Mathematica or any other mathematical software and displays the calculated result.

## Dependencies
- Uses mathpix to parse handwritten equation to latex
- Uses wolframclient (""[]) to evaluate expressions

https://github.com/xournalpp/xournalpp/issues/2747

https://xournalpp.github.io/guide/plugins/plugins/

```
npm install -g @mathpix/mpx-cli
mpx login
```
## TODO
- distribute into different folders (xournal, onenote, api)
- onenote plugin
- keep wolfram alive when not needed
- features
  - Numerical evaluation/rational evaluation
  - open context in wolfram
  
### Xournal
- UI
  - On/Off switch
  - Configuration button (path to wolfram,...)
  - Popup that shows detected latex expression and enables copying
  - Popup that shows calculated expression
  - option to open mathematica in current context

