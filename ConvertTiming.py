# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hour,minute,sec = s.strip().split(':') 
    if ('PM' in sec):
        if int(hour) != 12:
            hour = int(hour) + 12
        s = sec.split('PM')[0]
        return (':'.join([str(hour),str(minute),str(s)]))
    elif('AM' in sec):
        if int(hour) == 12:
            hour = int(hour)-12
            hour = '00'
        s = sec.split('AM')[0]
        return (':'.join([str(hour),str(minute),str(s)]))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')
    print(result)