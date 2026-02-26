import bcrypt

class Password:

  @staticmethod
  def check_pw(password, hashed):
    """
    Compare a plaintext password with a bcrypt hash.
    """
    if not isinstance(hashed, bytes):
      raise TypeError("hashed password must be bytes")

    return bcrypt.checkpw(password.encode("utf-8"), hashed)
  



  """
__ password.encode("utf-8")

password is your plain text password, like "mypassword123".
.encode("utf-8") converts the string into bytes, because bcrypt works with bytes, not Python strings.

password = "mypassword123"
password_bytes = password.encode("utf-8")

__ hashed

hashed is the password hash stored in your database.
Example (what bcrypt produces):

hashed = b"$2b$12$9uSg1b7G3xq.YeZ8cT6v4eF8hGq6Rvh0YhW5mZ7xXK1K5e2kYZJ6e"

This is already in bytes, typically returned by bcrypt.hashpw() when you first hashed the password.

__ bcrypt.checkpw(password_bytes, hashed)

bcrypt.checkpw() checks if the password matches the hash.
Returns True if the password is correct, False otherwise.


bcrypt automatically handles the salt stored in the hash. You don't need to save it separately.
  """