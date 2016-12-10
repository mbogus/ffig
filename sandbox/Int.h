#ifdef __clang__
#define C_API __attribute__((annotate("GENERATE_C_API")))
#else
#define C_API
#endif

class Int
{
  int value_ = 0;

public:
  Int(int value) : value_(value)
  {
  }

  Int plus(Int i) const
  {
    return Int(value_ + i.value_);
  }

  int value() const
  {
    return value_;
  }
} C_API;

