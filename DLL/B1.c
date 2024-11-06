#include <jni.h>
#include <stdio.h>
#include "B1.h"

JNIEXPORT jint JNICALL Java_B1_add(JNIEnv * env, jobject obj, jint a, jint b){
    printf("%d + %d = %d", a,b,(a+b));
}

JNIEXPORT jint JNICALL Java_B1_sub(JNIEnv *env, jobject obj, jint a, jint b){
    printf("%d + %d = %d", a,b,(a-b));
}

JNIEXPORT jint JNICALL Java_B1_mul(JNIEnv *env, jobject obj, jint a, jint b){
    printf("%d + %d = %d", a,b,(a*b));
}

JNIEXPORT jint JNICALL Java_B1_div(JNIEnv *env, jobject obj, jint a, jint b){
    printf("%d + %d = %d", a,b,(a/b));
}


