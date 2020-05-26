from pyautogui import keyDown, screenshot, press


keyDown('alt')
press('printscreen')
print(screen)
screen.save('testing.png')
