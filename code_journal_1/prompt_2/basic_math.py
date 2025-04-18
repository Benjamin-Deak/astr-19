def main():
    float1 = float(input("Enter a floating point number:"))
    float2 = float(input("Enter a second floating point number:"))
    sm = float1 + float2
    print(f"\nThe sum of your two inputs is {sm}")
    print(f"And it's type is {type(sm)}\n")

    int1 = int(input("Enter a integer:"))
    int2 = int(input("Enter a second integer:"))
    df = abs(int1 - int2)
    print(f"\nThe difference between your two inputs is {df}")
    print(f"And it's type is {type(df)}\n")

    float3 = float(input("Enter a floating point number:"))
    int3 = int(input("Enter an integer:"))
    prod = float3 * int3
    print(f"\nThe product of your two inputs is {prod}")
    print(f"And it's type is {type(prod)}\n")


main()