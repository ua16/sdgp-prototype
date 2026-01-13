<div class="w-full h-screen overflow-y-auto">
    <div
        class="text-black font-bold border-b-3 border-stone-300 bg-stone-100 p-2"
    >
        Send RFQ 
    </div>
    <div class="grid place-items-center bg-stone-200 pt-8">
        <form
            id="rfqForm"
            class="bg-stone-300 rounded-2xl text-lg text-black max-w-4xl mx-auto w-8/10 p-5 mb-5"
        >
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <!-- Origin -->
                <div class="space-y-2">
                    <label for="origin" class="block text-gray-800 font-medium"
                        >Origin *</label
                    >
                    <input
                        type="text"
                        id="origin"
                        name="origin"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Destination -->
                <div class="space-y-2">
                    <label
                        for="destination"
                        class="block text-gray-800 font-medium"
                        >Destination *</label
                    >
                    <input
                        type="text"
                        id="destination"
                        name="destination"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Cargo Type -->
                <div class="space-y-2">
                    <label
                        for="cargoType"
                        class="block text-gray-800 font-medium"
                        >Cargo Type *</label
                    >
                    <select
                        id="cargoType"
                        name="cargoType"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    >
                        <option value="">Select...</option>

                        <option value="FCL">FCL (Full Container Load)</option>
                        <option value="LCL"
                            >LCL (Less than Container Load)</option
                        >
                    </select>
                </div>

                <!-- Commodity -->
                <div class="space-y-2">
                    <label
                        for="commodity"
                        class="block text-gray-800 font-medium"
                        >Commodity *</label
                    >
                    <input
                        type="text"
                        id="commodity"
                        name="commodity"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- HS Code -->
                <div class="space-y-2">
                    <label for="hsCode" class="block text-gray-800 font-medium"
                        >HS Code *</label
                    >
                    <input
                        type="text"
                        id="hsCode"
                        name="hsCode"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Net Weight -->
                <div class="space-y-2">
                    <label
                        for="netWeight"
                        class="block text-gray-800 font-medium"
                        >Net Weight (kg) *</label
                    >
                    <input
                        type="number"
                        id="netWeight"
                        name="netWeight"
                        step="0.01"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Height -->
                <div class="space-y-2">
                    <label for="height" class="block text-gray-800 font-medium"
                        >Height (cm) *</label
                    >
                    <input
                        type="number"
                        id="height"
                        name="height"
                        step="0.01"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Width -->
                <div class="space-y-2">
                    <label for="width" class="block text-gray-800 font-medium"
                        >Width (cm) *</label
                    >
                    <input
                        type="number"
                        id="width"
                        name="width"
                        step="0.01"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Cargo Value -->
                <div class="space-y-2">
                    <label
                        for="cargoValue"
                        class="block text-gray-800 font-medium"
                        >Cargo Value ($) *</label
                    >
                    <input
                        type="number"
                        id="cargoValue"
                        name="cargoValue"
                        step="0.01"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Delivery Date -->
                <div class="space-y-2">
                    <label
                        for="deliveryDate"
                        class="block text-gray-800 font-medium"
                        >Delivery Date *</label
                    >
                    <input
                        type="date"
                        id="deliveryDate"
                        name="deliveryDate"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Issuing Organization ID -->
                <div class="space-y-2">
                    <label
                        for="issuingOrgID"
                        class="block text-gray-800 font-medium"
                        >Issuing Organization ID *</label
                    >
                    <input
                        type="number"
                        id="issuingOrgID"
                        name="issuingOrgID"
                        required
                        class="w-full px-4 py-3 rounded-lg border bg-stone-100 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                    />
                </div>

                <!-- Cargo Insurance Checkbox -->
                <div
                    class="flex items-center space-x-3 p-3 bg-white rounded-lg border border-gray-300"
                >
                    <input
                        type="checkbox"
                        id="needCargoInsurance"
                        name="needCargoInsurance"
                        class="w-5 h-5 text-blue-600 rounded bg-stone-100 focus:ring-blue-500"
                    />
                    <label
                        for="needCargoInsurance"
                        class="text-gray-800 font-medium cursor-pointer"
                    >
                        Need Cargo Insurance
                    </label>
                </div>

                <!-- Special Instructions (Full Width) -->
                <div class="md:col-span-2 space-y-2">
                    <label
                        for="specialInstructions"
                        class="block text-gray-800 font-medium"
                        >Special Instructions</label
                    >
                    <textarea
                        id="specialInstructions"
                        name="specialInstructions"
                        rows="4"
                        class="w-full px-4 py-3 rounded-lg bg-stone-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all resize-none"
                    ></textarea>
                </div>
            </div>

            <!-- Submit Button -->
            <div class="flex justify-center">
                <button
                    type="submit"
                    id="submitBtn"
                    class="rounded-lg text-blue-200"
                >
                    Submit Quote Request
                </button>
            </div>

            <!-- Status Message -->
            <div id="status" class="mt-6 text-center text-sm"></div>
        </form>
    </div>
</div>
