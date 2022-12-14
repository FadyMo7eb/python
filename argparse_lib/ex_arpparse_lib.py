"""
Arg Name or Optional Flags:
	positional	: str		= "foo"
	options		: str		= "-f", "--foo"

Standard:
	action		: str		= [store], append, store_true, store_false, store_const, append_const, version
	default		: *			= [None]
	type		: callable	= [str], argparse.FileType(mode='wb', bufsize=0)

Exotic:
	const		: *			= [None]
		Value to action="store_const" or action="append_const"
	choices		: indexable	= [None]
		Allowed values.
		ex: parser.add_argument( "-f", type=int, choices=(1,2,3) )
	nargs		: int		# require exactly N args
				: '?'		# default if opt is missing; const if opt is present; value if supplied with opt
				: '*'		# gather any args (after the opt, or positional)
				: '+'		# require 1+ and gather
		ex (int):
			parser.add_argument("-p", type="float", nargs=3, dest="point")
			$ feh.py -p 1 -3.5 4 ==> options.point = (1.0, -3.5, 4.0)
		ex (optional stdio):
			parser.add_argument('infile',  nargs='?', type=argparse.FileType('r'), default=sys.stdin)
			parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
	dest		: str		= [inferred]
	required	: bool		= [False]
	metavar		: str		= [inferred from name: "--foo-bar" -> "foo_bar"]
	help		: str		= [None]
		Specifiers: %(prog)s, and the keyword args here: 
		eg: %(default)s, %(metavar)s, %(type.__name__)s
	action		: callable
		ex:
			class FooAction(argparse.Action):
				def __call__(self, parser, namespace, values, option_string=None):
					print '%r %r %r' % (namespace, values, option_string)
					setattr(namespace, self.dest, values)


Usage:
	
	import argparse
	parser = argparse.ArgumentParser(
		description			= "can use %(default)s %(prog)s"
		epilog				= ''
		prog				= sys.argv[0]
		usage				= (generated)
		add_help			= True
		argument_default	= None
		parents				= None
		prefix_chars		= '-'
		conflict_handler	= None
		formatter_class		= 
	)
	parser.add_argument('--version', action='version', version='%(prog)s 2.0')
	parser.add_argument(name_or_flags[, ...], attr=value, ...)
	parser.set_defaults(arg=value)
	args = parser.parse_args()

"""