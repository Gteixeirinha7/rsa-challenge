# rsa-challenge

Programa desenvolvido em Python, tendo tido como referencia para desenvolver o codigo o link: https://hackingnaweb.com/criptografia/entendendo-algoritmo-rsa-de-verdade/
https://www.delftstack.com/howto/python/python-generate-prime-number/


Para executar o programa, tenha o Python3 instalado na maquina e com o repositorio aberto execute o comando:

" - py encode.py"

Apos isso digite a mensagem desejada, o sistema irá devolver a chave publica e a privada:

Exemplo:

" - Message encrypt: The information security is of significant importance to ensure the privacy of communications"
" - Public key: (5723, 299)"
" - Private key: (5723, 3203)"
" - Encrypted message: ޞѷ࡮ၪٖᓍఆൿݙҞᐕৼٖൿᓍၪۆ࡮ఫအݙٖৼേၪٖۆၪൿఆၪۆٖჽᓍٖఆٖఫᐕᓍৼၪٖҞখൿݙৼᐕᓍఫ࡮ၪৼൿၪ࡮ᓍۆအݙ࡮ၪৼѷ࡮ၪখݙٖ૕ᐕఫേၪൿఆၪఫൿҞҞအᓍٖఫᐕৼٖൿᓍۆ"

Apos isso sera perguntado se voce deseja decriptar a mensagem, se caso responder S, o sistema irá decriptar a mensagem

" - Gostaria de descriptar? (S/N)S"
" - Original message: The information security is of significant importance to ensure the privacy of communications"


Foi tambem desenvolvido um programa, que informando a mensagem encriptada, com a sua devida chave:

 - py decode.py 
 - Encrypted Message: ޞѷ࡮ၪٖᓍఆൿݙҞᐕৼٖൿᓍၪۆ࡮ఫအݙٖৼേၪٖۆၪൿఆၪۆٖჽᓍٖఆٖఫᐕᓍৼၪٖҞখൿݙৼᐕᓍఫ࡮ၪৼൿၪ࡮ᓍۆအݙ࡮ၪৼѷ࡮ၪখݙٖ૕ᐕఫേၪൿఆၪఫൿҞҞအᓍٖఫᐕৼٖൿᓍۆ
 - n value, private key: 5723
 - d value, private key: 3203
 - your original message: The information security is of significant importance to ensure the privacy of communications