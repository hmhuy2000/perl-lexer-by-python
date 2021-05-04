use strict;

sub parg {
    my($a, $b, $c) = @_;

    print "A: $a $b $c\n";
    print "B: $#_ [@_]\n\n";
}

parg("Hi", "there", "fred");

my @a1 = ("Today", "is", "the", "day");
parg(@a1);

parg("Me", @a1, "too");

my $joe = "sticks";
&parg ("Pooh $joe");

parg;

my @a2 = ("Never", "Mind");
parg @a2, "Boris", @a1, $joe;