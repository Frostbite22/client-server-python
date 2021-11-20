from twitter import *

t = Twitter(auth=OAuth('1229189739863068673-592ltN2QvlMXHRlx1qpX71NiWmhhUe',
                    'Bw28Hs3NNgrwqK8BjvUGu7lYpAvzpHnU3jADoYQkxVXgJ',
                    'iwPchwd9pvmCGfyIf3Htujuq1',
                    'Zk1N2oUCfPugrdGKMtjJ4h3fcFr08hYiH8O4egdAswI1PcAYHi'))

t.statuses.update(
    status=" From python twitter API.")


print(t.statuses.home_timeline())