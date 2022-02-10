#include<iostream>

int rev(int num)
{
    int rev_num = 0;
    while (num > 0)
    {
        rev_num = (rev_num * 10) + (num % 10);
        num /= 10;
    }
    return rev_num;
}

int main()
{
    unsigned long long int num;
    unsigned long long int m_num = 0;
    for (int i = 999; i > 100; --i)
    {
        for (int j = 999; j > 100; --j)
        {
            num = i * j;
            if (num == rev(num) && num > m_num)
            {
                m_num = num;
            }
        }
    }
    std::cout << m_num << '\n';
    return 0;
}