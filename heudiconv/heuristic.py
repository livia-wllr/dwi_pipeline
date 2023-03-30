import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    dwiRL3 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi287dirs3shb2000monop2s3_dir-RL_dwi')
    dwiLR4 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi287dirs3shb2000monop2s3_dir-LR_dwi')
    dwiRL5 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi196dirs2shb2000monop2s4_dir-RL_dwi')
    dwiLR7 = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-dwepi196dirs2shb2000monop2s4_dir-LR_dwi')
    
    
    


    info = {
            t1w: [],
            dwiRL3: [],
            dwiLR4: [],
            dwiRL5: [],
            dwiLR7: [],
            }


    #for s in seqinfo:
    for idx, s in enumerate(seqinfo):
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

        if ('sub-5876_ses-10405_T1w' in s.series_description):
            info[t1w].append(s.series_id)
        if ('sub-5876_ses-10405_acq-dwepi287dirs3shb2000monop2s3_dir-RL_dwi' in s.series_description):
            info[dwiRL3].append(s.series_id)
        if ('sub-5876_ses-10405_acq-dwepi287dirs3shb2000monop2s3_dir-LR_dwi' in s.series_description):
            info[dwiLR4].append(s.series_id)
        if ('sub-5876_ses-10405_acq-dwepi196dirs2shb2000monop2s4_dir-RL_dwi' in s.series_description):
            info[dwiRL5].append(s.series_id)
        if ('sub-5876_ses-10405_acq-dwepi196dirs2shb2000monop2s4_dir-LR_dwi' in s.series_description):
            info[dwiLR7].append(s.series_id)
        
    return info
