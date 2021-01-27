def money():
    FIRST = 12345
    SECOND = 1234567

    m_first = 0
    m_second = 0

    val_first = 0
    val_second = 0
    while (val_first-1 != val_second):
        if val_first > val_second:
            val_second += SECOND
            m_second += 1
        else:
            val_first += FIRST
            m_first += 1
            
    return (m_first, m_second)

print(money())