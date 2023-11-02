from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession()

print(session.evaluate(wlexpr('Range[5]')))
print(session.evaluate(wl.MinMax([1, -3, 0, 9, 5])))
# print(func_squared = wlexpr('#^2 &'))
# print(session.evaluate(wl.Map(func_squared, wl.Range(5))))