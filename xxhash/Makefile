CXX = g++
CXXFLAGS = -std=c++11 -I/home/chris/Hashing/booksim2/hash_study/vcpkg/installed/x64-linux/include
LDFLAGS = -L/home/chris/Hashing/booksim2/hash_study/vcpkg/installed/x64-linux/lib -lxxhash
TARGET = try

all: $(TARGET)

$(TARGET): try.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) try.cpp $(LDFLAGS)

clean:
	rm -f $(TARGET)