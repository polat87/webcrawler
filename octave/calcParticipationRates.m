%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%						  Participation Rates						   %
%						GOEKHAN POLAT (0830690)						   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% TODO: implement a function that calculates the average rate of participation and average size of events
% INPUT: adjacency matrix (mxn) of the two-mode network
% OUTPUT: participation rate values (doubles)
function [avg_size_of_events, avg_rate_of_participation] = calcParticipationRates(network)
	edges = sum(sum(network));
	rows = size(network)(1);
	cols = size(network)(2);	
    avg_size_of_events = edges / cols;
    avg_rate_of_participation = edges / rows;
end
