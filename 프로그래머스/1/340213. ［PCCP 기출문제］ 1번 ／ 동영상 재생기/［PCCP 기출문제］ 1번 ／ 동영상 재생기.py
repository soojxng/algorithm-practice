def t_to_i(t):
    m, s = t.split(':')
    i = int(m) * 60 + int(s)
    return i

def i_to_t(i):
    m = i // 60
    s = i - m * 60
    t = ("0" if m < 10 else "") + str(m) + ":" + ("0" if s < 10 else "") + str(s)
    return t

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = t_to_i(video_len)
    op_start = t_to_i(op_start)
    op_end = t_to_i(op_end)
    c_dict = {"next" : 10, "prev" : -10}
    now = t_to_i(pos)
    now = op_end if now >= op_start and now < op_end else now
    
    for c in commands:
        now += c_dict[c]
        if now < 0:
            now = 0
        if now > video_len:
            now = video_len
        if now >= op_start and now < op_end:
            now = op_end
    return i_to_t(now)