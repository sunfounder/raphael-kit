# sample makefile
CC = gcc
CFLAGS = -Wall -std=c11
OUTFILE = 1.1.6_LedMatrix
OBJS = 1.1.6_LedMatrix.o
SRCS = 1.1.6_LedMatrix.c

$(OUTFILE): $(OBJS)
	$(CC) $(CFLAGS) -o $(OUTFILE) $(OBJS) -lbcm2835
$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS)

clean:
	rm -f $(OBJS) $(OUTFILE)

.PHONY : all
all : $(OUTFILE)
