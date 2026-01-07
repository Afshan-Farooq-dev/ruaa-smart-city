import inspect

try:
    from groq import Groq
    print('Groq imported from:', Groq.__module__)
    try:
        sig = inspect.signature(Groq)
    except Exception as e:
        sig = f'Could not get signature: {e}'
    print('Groq signature:', sig)
    try:
        src = inspect.getsource(Groq)
        print('\n--- Groq source preview (first 400 chars) ---')
        print(src[:400])
    except Exception as e:
        print('Could not read Groq source:', e)
except Exception as e:
    print('Error importing Groq:', e)
