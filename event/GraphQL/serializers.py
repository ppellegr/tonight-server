class CreateCouponSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = CouponSerializer

    @classmethod
    @permission_checker(['coupons.add_coupon'])
    def mutate_and_get_payload(cls, root, info, **input):
        return super(CouponSerializerMutation, cls).mutate_and_get_payload(root, info, **input)
