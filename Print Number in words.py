def num_to_word(num):
    A={
        '1':'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five',
        '6':'Six',
        '7':'Seven',
        '8':'Eight',
        '9':'Nine',
        '10':'Ten'
    }
    
    digit=str(num)
    for i in digit:
        word=A.get(i)
        if word:
            print(word, end=' ')
            
num=int(input("Enter A number"))
num_to_word(num)
