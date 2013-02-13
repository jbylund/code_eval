#!/usr/bin/perl
use strict;

for(my $outer = 1; $outer <= 12; $outer++)
{
    for(my $inner = 1; $inner <= 12; $inner++)
    {
        if($inner > 1)
        {
            printf("%4d",$outer*$inner);
        }
        else
        {
            my $line = sprintf("%4d",$outer*$inner);
            $line =~ s/^\s+//;
            print $line;
        }
    }
    print "\n";
}

