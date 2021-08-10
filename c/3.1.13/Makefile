# sample makefile
CC = gcc
CFLAGS = -Wall -std=c11
OUTFILE = 3.1.13_GAME_NotNot
OBJS = 3.1.13_GAME_NotNot.o
SRCS = 3.1.13_GAME_NotNot.c

$(OUTFILE): $(OBJS)
	$(CC) $(CFLAGS) -o $(OUTFILE) $(OBJS) -lbcm2835
$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $(SRCS)

clean:
	rm -f $(OBJS) $(OUTFILE)

.PHONY : all
all : $(OUTFILE)
