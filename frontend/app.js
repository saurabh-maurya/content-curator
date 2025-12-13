// Frontend JavaScript for Instagram AI Avatar Automation

const API_BASE_URL = 'http://localhost:8000';
let currentSessionId = null;
let checklistItems = [];

// Initialize on page load
document.addEventListener('DOMContentLoaded', async () => {
    await loadConfig();
});

// Load configuration (models, content types, checklist)
async function loadConfig() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/config`);
        const data = await response.json();
        
        // Populate API model dropdown
        const modelSelect = document.getElementById('apiModel');
        modelSelect.innerHTML = '<option value="">Select API Model</option>';
        data.models.forEach(model => {
            const option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            if (model === 'gpt-4o-mini') {
                option.selected = true;
            }
            modelSelect.appendChild(option);
        });
        
        // Populate content type dropdown
        const typeSelect = document.getElementById('contentType');
        typeSelect.innerHTML = '<option value="">Select Content Type</option>';
        data.content_types.forEach(type => {
            const option = document.createElement('option');
            option.value = type;
            option.textContent = type;
            typeSelect.appendChild(option);
        });
        
        // Store checklist items
        checklistItems = data.checklist;
        
    } catch (error) {
        console.error('Error loading config:', error);
        showError('Failed to load configuration. Make sure the backend is running.');
    }
}

// Create content
async function createContent() {
    const apiKey = document.getElementById('apiKey').value;
    const apiModel = document.getElementById('apiModel').value;
    const topic = document.getElementById('topic').value;
    const contentType = document.getElementById('contentType').value;
    
    // Validation
    if (!apiKey || !apiModel || !topic || !contentType) {
        showError('Please fill in all required fields.');
        return;
    }
    
    // Hide previous results
    document.getElementById('resultsSection').style.display = 'none';
    document.getElementById('checklistSection').style.display = 'none';
    document.getElementById('errorContainer').innerHTML = '';
    
    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('createBtn').disabled = true;
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/create-content`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                topic: topic,
                content_type: contentType,
                api_key: apiKey,
                api_model: apiModel,
            }),
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.detail || 'Content creation failed');
        }
        
        // Store session ID
        currentSessionId = data.session_id;
        
        // Display results
        displayResults(data.result);
        displayChecklist(data.result.checklist_status);
        
        // Show sections
        document.getElementById('resultsSection').style.display = 'block';
        document.getElementById('checklistSection').style.display = 'block';
        
    } catch (error) {
        console.error('Error creating content:', error);
        showError(`Failed to create content: ${error.message}`);
    } finally {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('createBtn').disabled = false;
    }
}

// Display results
function displayResults(result) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    
    // Script/Content
    if (result.script) {
        const scriptDiv = document.createElement('div');
        scriptDiv.className = 'result-item';
        scriptDiv.innerHTML = `
            <h3>📝 Script</h3>
            <pre>${escapeHtml(result.script)}</pre>
        `;
        resultsDiv.appendChild(scriptDiv);
    }
    
    // Carousel Content
    if (result.carousel_content) {
        const carouselDiv = document.createElement('div');
        carouselDiv.className = 'result-item';
        carouselDiv.innerHTML = `
            <h3>📚 Carousel Content</h3>
            <pre>${escapeHtml(result.carousel_content)}</pre>
        `;
        resultsDiv.appendChild(carouselDiv);
    }
    
    // Caption
    if (result.caption) {
        const captionDiv = document.createElement('div');
        captionDiv.className = 'result-item';
        captionDiv.innerHTML = `
            <h3>✍️ Caption</h3>
            <pre>${escapeHtml(result.caption)}</pre>
        `;
        resultsDiv.appendChild(captionDiv);
    }
    
    // Hashtags
    if (result.hashtags) {
        const hashtagsDiv = document.createElement('div');
        hashtagsDiv.className = 'result-item';
        hashtagsDiv.innerHTML = `
            <h3>🏷️ Hashtags</h3>
            <pre>${escapeHtml(result.hashtags)}</pre>
        `;
        resultsDiv.appendChild(hashtagsDiv);
    }
    
    // Alt Text
    if (result.alt_text) {
        const altTextDiv = document.createElement('div');
        altTextDiv.className = 'result-item';
        altTextDiv.innerHTML = `
            <h3>🔍 Alt Text</h3>
            <pre>${escapeHtml(result.alt_text)}</pre>
        `;
        resultsDiv.appendChild(altTextDiv);
    }
    
    // Avatar Dialogue
    if (result.avatar_dialogue) {
        const dialogueDiv = document.createElement('div');
        dialogueDiv.className = 'result-item';
        dialogueDiv.innerHTML = `
            <h3>🧍 Avatar Dialogue</h3>
            <pre>${escapeHtml(result.avatar_dialogue)}</pre>
        `;
        resultsDiv.appendChild(dialogueDiv);
    }
}

// Display checklist
function displayChecklist(checklistStatus) {
    const checklistDiv = document.getElementById('checklist');
    checklistDiv.innerHTML = '';
    
    checklistItems.forEach(item => {
        const status = checklistStatus[item.id] || 'pending';
        const itemDiv = document.createElement('div');
        itemDiv.className = `checklist-item ${status}`;
        
        const statusBadge = getStatusBadge(status);
        
        itemDiv.innerHTML = `
            <div class="checklist-info">
                <h4>${item.name} ${statusBadge}</h4>
                <p>${item.description}</p>
            </div>
            <div class="checklist-actions">
                ${item.automated ? '' : '<button class="btn-small btn-manual" onclick="markAsManual(\'' + item.id + '\')">Mark Manual</button>'}
                <button class="btn-small btn-complete" onclick="markAsComplete(\'' + item.id + '\')">Mark Complete</button>
            </div>
        `;
        
        checklistDiv.appendChild(itemDiv);
    });
}

// Get status badge HTML
function getStatusBadge(status) {
    const badges = {
        'pending': '<span class="status-badge status-pending">Pending</span>',
        'completed': '<span class="status-badge status-completed">Completed</span>',
        'failed': '<span class="status-badge status-failed">Failed</span>',
        'manual': '<span class="status-badge status-manual">Manual</span>',
    };
    return badges[status] || badges['pending'];
}

// Mark checklist item as manual
async function markAsManual(taskId) {
    await updateChecklist(taskId, 'manual');
}

// Mark checklist item as complete
async function markAsComplete(taskId) {
    await updateChecklist(taskId, 'completed');
}

// Update checklist status
async function updateChecklist(taskId, status) {
    if (!currentSessionId) {
        showError('No active session. Please create content first.');
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/checklist/${currentSessionId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                task_id: taskId,
                status: status,
            }),
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Reload checklist display
            displayChecklist(data.checklist_status);
        }
    } catch (error) {
        console.error('Error updating checklist:', error);
        showError('Failed to update checklist.');
    }
}

// Show error message
function showError(message) {
    const errorContainer = document.getElementById('errorContainer');
    errorContainer.innerHTML = `<div class="error">${escapeHtml(message)}</div>`;
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

