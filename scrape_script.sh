rm headers_and_cookies
rm output*
echo "done"
curl --dump-header headers_and_cookies -vk -d "x=34&y=13&scheme=http&username=dukehg30&password=skarlath5"  https://duke.experience.com/er/security/login.jsp --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1"
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201107 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output07
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201108 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output08
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201109 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output09
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201110 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output10
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201111 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output11
curl --cookie  headers_and_cookies -kv   https://duke.experience.com/er/stu/calendar/career_center_calendar_view.jsp?date=201112 --user-agent "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1" > output12

