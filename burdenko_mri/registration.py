import ants


def rigid_reg(fixed:str, moving:str, mask:str=None):
    ants_fixed = ants.image_read(fixed)
    ants_moving = ants.image_read(moving)
    
    res = ants.registration(fixed=ants_fixed, moving=ants_moving,
                            type_of_transform='Rigid')
    transform = ants.read_transform(res['fwdtransforms'][0])
    ants_warped = ants.apply_ants_transform(transform, ants_moving,
                                         data_type='image', reference=ants_fixed)
    if mask is not None:
        ants_mask_fixed = ants.image_read(mask)
        warped_mask = ants.apply_ants_transform(transform, ants_mask_fixed,
                                         data_type='image', reference=ants_fixed)
        return ants_warped, warped_mask
    return ants_warped