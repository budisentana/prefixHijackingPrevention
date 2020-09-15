import schedule

def thing_you_wanna_do():
    print ('test')
    return


schedule.every().second.do(thing_you_wanna_do)

while True:
    schedule.run_pending()