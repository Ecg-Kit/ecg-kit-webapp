import wfdb, sys

def main(argv):
    siarray = wfdb.isigopen("100s")
    if siarray.nsig < 2: sys.exit(1)
    v = wfdb.WFDB_SampleArray(2)
    for i in range(0,10):
        if wfdb.getvec(v.cast()) < 0: sys.exit(2)
        print "\t%d\t%d" % (v[0], v[1])

if __name__ == "__main__":
    main(sys.argv[1:])
