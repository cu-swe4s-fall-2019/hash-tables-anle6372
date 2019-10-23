

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test1 bash benchmark.sh
assert_no_stdout
assert_no_stderr
