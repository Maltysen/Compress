#Compress

##A language for kolmogrov-complexity challenges

##What is Compress?

Compress is a new programming language that seeks to eliminate the boilerplate in using other languages to make lookup tables in kolmogrov complexity.

##What makes Compress Special?

In Compress, one doesn't have to specify a lookup table. Just make a list of tokens, and the translation table is *implicitly generated* for you. Here is an example:

##Examples

    "Hello" and

    Bob says "Hello" and "Nice to see you" and Mary shouts "Hello" back.

This is a completely valid Compress program. Save it as `test.cmpr` and run with `python3 compress.py -o test.cmpr` (the `-o` flag is for `one-file` mode) to get the output.
Here is the output:

    Bob says   ¡ "Nice to see you" ¡ Mary shouts   back.

The table at the top which contains the tokens `"Hello"` and `and` gets converted to a lookup table where those two are converted to the first two latin-1 tokens.

So the actual code you would use would be

	"Hello" and

	Bob says   ¡ "Nice to see you" ¡ Mary shouts   back.

Save as a `latin-1` encoded file and run it with the same command and it detects the presence of non ascii characters and assumes that you want the lookup table to go in the opposite direction - no flags needed!

##Processing

This also supports pre-processing and post-processing of the data. Just put an arbitrary python expression right under the table and it'll act as either pre or post processing depending on the way the lookup table is going.