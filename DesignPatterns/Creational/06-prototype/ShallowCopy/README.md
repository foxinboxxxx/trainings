issue: mainboard of T1 was also changed to Business, because of shallow copy
shallow copy constructs a new compound object and than inserts references
into it to the objects found in original

shallow cloning, which just copies the references of objects in the instance to be cloned

To fix: use deep cloning