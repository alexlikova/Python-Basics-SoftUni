broiStr = int(input());
pages = int(input());
dni = int(input());

readTime = broiStr / pages;
readPerDay = readTime / dni;

print(readPerDay);