<?php

session_start();

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
    return $copilot_skills[$copilot_id]["skills"][$skill_name] ?? null;
}

function intro() {
    echo "<h2>Welcome to the Adventure Game!</h2>";
    echo "<p>You find yourself at the entrance of a dark cave.</p>";
    echo '<form method="post"><input type="submit" name="action" value="Enter Cave"></form>';
    echo '<form method="post"><input type="submit" name="action" value="Stay Outside"></form>';
}

function enterCave() {
    echo "<h2>You step into the cave and it's pitch black.</h2>";
    echo '<form method="post"><input type="submit" name="action" value="Light Torch"></form>';
    echo '<form method="post"><input type="submit" name="action" value="Stay in the Dark"></form>';
}

function lightTorch() {
    echo "<h2>With the torch lit, you can see the cave walls are lined with ancient carvings.</h2>";
    echo '<form method="post"><input type="submit" name="action" value="Explore Further"></form>';
    echo '<form method="post"><input type="submit" name="action" value="Leave"></form>';
}

function exploreFurther() {
    echo "<h2>You explore further and find a hidden treasure!</h2>";
    echo '<form method="post"><input type="submit" name="action" value="Take Treasure"></form>';
    echo '<form method="post"><input type="submit" name="action" value="Leave"></form>';
}

function takeTreasure() {
    echo "<h2>Congratulations! You have taken the treasure and completed the adventure!</h2>";
}

// Assign the adventure game skill to Copilot
assign_skill_to_copilot("36f33bbb-4dd7-4a68-a5b8-56c7c3c32d5b", "adventure_game", "intro");

// Handle form submissions
$action = $_POST['action'] ?? null;
$copilot_id = "36f33bbb-4dd7-4a68-a5b8-56c7c3c32d5b";
$skill_name = "adventure_game";

$skill_function = get_copilot_skill($copilot_id, $skill_name);
if ($skill_function) {
    switch ($action) {
        case "Enter Cave":
            enterCave();
            break;
        case "Light Torch":
            lightTorch();
            break;
        case "Explore Further":
            exploreFurther();
            break;
        case "Take Treasure":
            takeTreasure();
            break;
        default:
            call_user_func($skill_function);
            break;
    }
} else {
    echo "Skill not found for this Copilot.\n";
}

?>