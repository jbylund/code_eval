#!/usr/bin/perl
use strict;

my $filesize = -s $ARGV[0];
print "$filesize\n";
