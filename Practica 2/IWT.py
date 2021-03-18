#Author Dion Tzamarias
#Integer Wavelet Transform Library

import numpy as np
import math
#from PIL import Image

def DF_iwt_1D(X):
        nl, nc = X.shape
        Y = np.zeros([nl,nc])

        if nc//2.0 == nc/2.0:
                k = int(nc/2)
               
                for l in range(nl):
                        Y[l, 1:(2*k-2):2] = X[l, 1:(2*k-2):2] - np.floor((X[l, 0:(2*k-3):2] + X[l, 2:(2*k-1):2])/2.0) 
                        Y[l, 2*k-1] = X[l, 2*k-1] - X[l, 2*k-2]

                for l in range(nl):
                        Y[l, 0] = X[l, 0] + np.floor(Y[l, 1]/2.0)
                        Y[l, 2:(2*k-1):2] = X[l, 2:(2*k-1):2] + np.floor((Y[l, 1:(2*k-2):2] + Y[l, 3:(2*k):2])/4.0)

        elif nc//2.0 != nc/2.0:
                k = int((nc-1)/2)
                for l in range(nl):
                        Y[l, 1:(2*k):2] = X[l, 1:(2*k):2] - np.floor((X[l, 0:(2*k-1):2] + X[l, 2:(2*k+1):2])/2.0)

                for l in range(nl):
                        Y[l, 0] = X[l, 0] + np.floor((Y[l, 1])/2.0)
                        Y[l, 2*k] = X[l, 2*k] + np.floor((Y[l, 2*k-1])/2.0)
                        Y[l, 2:(2*k-1):2] = X[l, 2:(2*k-1):2] + np.floor((Y[l, 1:(2*k-2):2] + Y[l, 3:(2*k):2])/4.0)

        return Y

def DF_rearange_im(A):
        nl, nc = A.shape
        B = np.zeros([nl, nc])

        LL = np.array(A[0::2, 0::2])
        LH = np.array(A[0::2, 1::2])
        HL = np.array(A[1::2, 0::2])
        HH = np.array(A[1::2, 1::2])

        l_tmp, c_tmp = LL.shape
        B[0:l_tmp,0:c_tmp] = LL

        B[0:l_tmp,c_tmp:] = LH

        B[l_tmp:,0:c_tmp] = HL

        B[l_tmp:,c_tmp:] = HH

        return B, l_tmp, c_tmp

def DF_iwt2D(A, levels):
        nl, nc = A.shape
        R = np.zeros([nl, nc])
        l_tmp0 = nl
        c_tmp0 = nc
        C_tmp = np.zeros([nl, nc])
        C_tmp = A
        count = levels
        while count>0:
                B_tmp = DF_iwt_1D(DF_iwt_1D(C_tmp).T).T
                R_tmp, l_tmp, c_tmp = DF_rearange_im(B_tmp)
                R[0:l_tmp0, 0:c_tmp0] = R_tmp
                C_tmp = R_tmp[0:l_tmp, 0:c_tmp]
                l_tmp0 = l_tmp
                c_tmp0 = c_tmp
                count = count -1
        return R


def DF_entropy(lst):
        res = sum([-i*math.log(i, 2) for i in lst])
        return res

def img_info(np_arr):
        num_ln, num_cl = np_arr.shape
        tot_elz = float(num_ln*num_cl)
        uni_pikz, cntz = np.unique(np_arr, return_counts = True)
        py_uni_pikz = [str(x) for x in list(uni_pikz)]
        py_cntz = list(cntz/tot_elz)
        dct = dict(zip(py_uni_pikz, py_cntz))
        entr = DF_entropy(dct.values())
        return (dct, entr)

def iwt(np_arr0, levels):
        np_arr = np.int64(np_arr0)
        outp_tmp = DF_iwt2D(np_arr, levels)
        outp = outp_tmp.astype(int)
        #Image.fromarray(np.int32(outp)).show('im1') 
        dct, entr = img_info(outp)
        return (dct, entr)
