"""
**** warning ****

When you say import in Python, the interpreter runs a search to find a file with that name. It first looks for the file in the current folder and then in other paths, such as, /usr/lib/python.

Therefore, when you're saying import argparse and naming your script argparse.py, Python takes your file and import it as is.

To avoid this, change the name of your file to something else than argparse.py.



** parser.add_argument ** = [
            || "the_arguments_you_write" 
            || dest = "the_frist_argument_have ( -- )  Note : the dest is the value will apper in parse_args " 
            || nargs = * => for unlimited argument , ? => for one argument , (1,2,3,....) => for num of argument , + => like * but you should at least pass one argument 
            || action = store => This just stores the arguments value. This is the default action 
            || store_const => This stores the value specified by the const keyword argument. most commonly used with optional arguments that specify some sort of flag
            || store_true // store_false => if you write the command it will kept true or flase just you write it 
            || append => when the argument repeat many times with one vlaue ex: --foo 1 --foo 2 --foo 3 
            || append_const => this tell you the gen of the vlaue append on const ex: '--str', dest='types', action='append_const', const=str
            || count => to count the times you write the argument like verbos ex: -v -vv -vvv -vvvv
            || version => if you wanna to write your tool ver ex: parser =  argparse.ArgumentParser(prog="Prog")
                                                                            parser.add_argument('--version', action='version', version='%(prog)s 2.0')
            || extend => to save vlaues in list if it repeated more one time 
            || help => to write help content and write the argument ex: -h --help
            || type => int,string,None,float,...... to specific type to get in 
            || choices =>["you but here some choices that the user must choose one of them " ]
            || default => a value but automatic it the user didn't write it or value like True , Flase ** if you wanna to put no value at all  " default=argparse.SUPPRESS "
            || metavar => The metavar option gives a name to the expected value in error and help outputs.
                            ]

**argparse.ArgumentParser ** = [
            || prog => the name of program // recomended os.path.basename(sys.argv[0])
            || usage => to write of the usage of your program
            || description => the description will apper after usage 
            || epilog => this massage will apper to the end of help 
            || prefix_chars => the append an ch befor the command ex: -ls > +ls 
            || add_help => False,True to show -h , --help in help menu or not 
                                ]


** parser.parse_args() ** = [
            NOTE  : you can put args like that " -x y" or " --xel y " or " --xel=y " or "-xy" 
            NOTE  : you can concatenate some argument with true or flase const_sotre ex: 
                                                    >>> parser = argparse.ArgumentParser(prog='PROG')
                                                    >>> parser.add_argument('-x', action='store_true')
                                                    >>> parser.add_argument('-y', action='store_true')
                                                    >>> parser.add_argument('-z')
                                                    >>> parser.parse_args(['-xyzZ'])
                                                    Namespace(x=True, y=True, z='Z')
            

            
"""
