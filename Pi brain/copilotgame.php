<?php

$copilot_skills = [
    "36f33bbb-4dd7-4a68-a5b8-56c7c3c32d5b" => [
        "skills" => ["adventure_game" => "intro"]
    ]
];

function assign_skill_to_copilot($copilot_id, $skill_name, $skill_function) {
    global $copilot_skills;
    $copilot_skills[$copilot_id]["skills"][$skill_name] = $skill_function;
}

function get_copilot_skill($copilot_id, $skill_name) {
    global $copilot_skills;
    if (isset($copilot_skills[$copilot_id]["skills"][$skill_name])) {
        return $copilot_skills[$copilot_id]["skills"][$skill_name];
    }
    return null;
}

function intro() {
    echo "Welcome to the Adventure Game!\n";
    echo "You find yourself at the entrance of a dark cave.\n";
    $choice = readline("Do you want to enter the cave? (yes/no): ");
    
    if (strtolower($choice) == "yes") {
        enterCave();
    } else {
        echo "You decided to stay outside. The adventure ends here.\n";
    }
}

function enterCave() {
    echo "You step into the cave and it's pitch black.\n";
    $choice = readline("Do you want to light a torch? (yes/no): ");
    
    if (strtolower($choice) == "yes") {
        lightTorch();
    } else {
        echo "You stumble in the dark and fall into a pit. Game over.\n";
    }
}

function lightTorch() {
    echo "With the torch lit, you can see the cave walls are lined with ancient carvings.\n";
    $choice = readline("Do you want to explore further or leave? (explore/leave): ");
    
    if (strtolower($choice) == "explore") {
        echo "You discover a hidden treasure chest filled with gold!\n";
    } else {
        echo "You leave the cave, missing out on potential treasures.\n";
    }
}

// Assign the adventure game skill to Copilot
assign_skill_to_copilot("36f33bbb-4dd7-4a68-a5b8-56c7c3c32d5b", "adventure_game", "intro");

// Example of how a Copilot might call the skill
$copilot_id = "36f33bbb-4dd7-4a68-a5b8-56c7c3c32d5b";
$skill_name = "adventure_game";

$skill_function = get_copilot_skill($copilot_id, $skill_name);
if ($skill_function) {
    call_user_func($skill_function);
} else {
    echo "Skill not found for this Copilot.\n";
}

?>
