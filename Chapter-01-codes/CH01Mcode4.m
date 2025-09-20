%this M-file, named CH01Mcode4.m,
% calculates the time taken to 
% fill Craig Goch reservoir (UK)
clc ; % clear screen
clear ; % clear memory
V=9.2*(10^6);%reservoir volume (m3)
q=5; % river dischage (m3/s)
% Initialize variables
volume=0;%reservoir starting volume
time = 0;    % Time (seconds)
% while loop, time taken to fill dam
while volume < V
 volume = volume + q;% volume added
 time = time + 1;%time increment:1 sec
end
% Convert time from seconds to days
time_days = time / (60 * 60 * 24);
% Display result
display(time_days);
% end of M - file
