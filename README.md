# cognition
Cognitive and memory model experiments


1. Memory degradation models
2. Memory degradation + refresh models
3. Associative access
4. Associative event reconstruction
5. Timeline Construction


1. Memory Degradation Model

A placeholder approach for now. Take the image, make a copy. One copy, guassian blur. Second copy, edge detecd. Adjust edge detect to have "right" colors, based on original. Add the two images together. 

2. Refresh Model

Add paramter for edge detect sensitivity. Scale 0-100 (100 being most sensitive). Start with sensitivity 10. With each refresh in a time interval Tint < Threshold_refresh, bump the detect sensitivity by +5. With each lack of refresh in a time interval > Threshold_Remember, decrease the sensitivity by -5.

3. Associative Access

4. Associative event reconstruction

Foundational objects and processes for step 5...timeline construction, which is where the dream sequence is generated.

5. Timeline Construction

This requires a lot of thought. Keyframes plus interpolation. Associative access. This is where we build the dream, but where does the timeline come from? Need a way to create new memories that stores "video" as a timeline construct, with degradation capability. This is the enchilada.



Notes and Sources
=================


Tufts faces dataset acknowledgement...

- Website: http://tdface.ece.tufts.edu/ and 

- Paper: Panetta, Karen, Qianwen Wan, Sos Agaian, Srijith Rajeev, Shreyas Kamath, Rahul Rajendran, Shishir Rao et al. "A comprehensive database for benchmarking imaging systems." IEEE Transactions on Pattern Analysis and Machine Intelligence (2018).

Download link, after registration:
http://tdface.ece.tufts.edu/downloads/

.dat for DLIB face feature predictor (there are many other possibilities, this is a 68-point version of unclear history

https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
