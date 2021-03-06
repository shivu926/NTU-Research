

#ifndef _TRIANGULATE_H
#define _TRIANGULATE_H

#include <vector>
#include <assert.h>

#include "AGVector.h"

using std::vector;

class Triangulate {

public:
   // Puts vertices of triangulation of polygon into result.
   static bool Process( vector<AGVector> &polygon, vector<AGVector *> &result);
	
   // Returns area of polygon.
   static float Area(const vector<AGVector> &polygon);
	
   // True if p is inside triangle(abc).
   static bool InsideTriangle(AGVector a, AGVector b, AGVector c, AGVector p);

private:
   // True if points p1 and p2 are on the same side of line segment ab.
   static bool SameSide(AGVector a, AGVector b, AGVector p1, AGVector p2);

   /* 
    * Determines if the section of the polygon defined by the three vertices
    * abc (where abc are at indices u,v,w in polygon) can be
    * 'snipped' (considered a triangle in the triangulation of the polygon).
    * True if abc is convex and empty, false if another vertex of the polygon lies within
    * abc, or if abc forms a right turn (non-convex, assuming counter clockwise (ccw) traversal).
    * V is an array of integers, containing the indices of polygon in ccw order, n is its length
    */
    static bool Snip(const vector<AGVector *> &polygon, int u, int v, int w);
};

#endif /* _TRIANGULATE_H */
