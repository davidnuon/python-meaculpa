#!/usr/bin/env python
import time, cgi, cgitb
names = ["nathangubb", "Edavidburg", "smarty", "dn_desaku", "Dr Small", "NovaAesa", "fedex", "sonicrules1234"]
bdays = ["April 20 93", "April 18 91", "April 19 92", "September 8 93", "March 19 91", "June 14 89", "February 10 93", "March 17 92"]
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def main() :
    print "Content-Type: text/html\n"
    count = 0
    for birthday in bdays :
        bday = time.strptime(birthday, "%B %d %y")
        now = time.gmtime()
        if bday[1] < now[1] or bday[1] == now[1] and bday[2] <= now[2] :
            years = now[0] - bday[0]
            if bday[1] == now[1] :
                if bday[2] == now[2] :
                    months = 0
                    days = 0
                elif bday[2] > now[2] :
                    months = 11
                    days = bday[2] - now[2]
                elif bday[2] < now[2] :
                    months = 0
                    days = now[2] - bday[2]
            elif bday[1] < now[1] :
                if bday[2] == now[2] :
                    months = now[1] - bday[1]
                    days = 0
                elif bday[2] < now[2] :
                    months = now[1] - bday[1]
                    days = now[2] - bday[2]
                elif bday[2] > now[2] :
                    month = bday[1] - now[1]
                    days = bday[2] - now[2]
        else :
            years = now[0] - bday[0] - 1
            if bday[2] == now[2] :
                months = 12 - bday[1] - now[1]
                days = 0
            elif bday[2] > now[2] :
                months = (11 - bday[1]) + now[1]
                days = m[bday[1] - 2] + bday[2]
            elif bday[2] < now[2] :
                months = 12 - bday[1] - now[1]
                days = now[2] - bday[2]
        print "<p>%s is %s years, %s month(s), and %s day(s) old.</p>\n" % (names[count], str(years), str(months), str(days))
        count = count + 1


if __name__ == "__main__" : main()