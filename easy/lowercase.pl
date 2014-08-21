#!/usr/bin/perl
use strict;

open my $fh, $ARGV[0] or die("Could not open  file.");

while(my $line = <$fh>)
{
    print lc($line);
}
