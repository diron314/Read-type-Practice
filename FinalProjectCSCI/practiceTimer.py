from threading import Timer

timeout = 5
t = Timer(timeout, print, ['Times up!'])
print(type(t))
print("")
t.start()
textToCopy = "Here is example text.\n" .format(timeout)
answer = input(textToCopy)
t.cancel()
